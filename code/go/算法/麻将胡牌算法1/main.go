package main

import (
	"fmt"
	"time"
)

const (
	IndexMax   = 34
	MagicIndex = 31
	KindMax    = 4
	//
	WanMax  = 9
	TiaoMax = 18
	TongMax = 27
	//
	LeftChi   = 0x1
	RightChi  = 0x2
	CenterChi = 0x4
	Peng      = 0x8
	Gang      = 0x10
	Jiang     = 0x20
)

type KindItem struct {
	Kind       int
	MagicCount int
	CenterCard int
	Data       [3]int
}

func (c *KindItem) Set(kind int, magicCount int, centerCard int, data [3]int) {
	c.Kind = kind
	c.MagicCount = magicCount
	c.CenterCard = centerCard
	c.Data = data
}
func (c *KindItem) String() string {
	if c.Kind == Jiang {
		return fmt.Sprintf("[%d %d -(%d)]", c.Data[0], c.Data[1], c.MagicCount)
	} else {
		return fmt.Sprintf("[%d %d %d(%d)]", c.Data[0], c.Data[1], c.Data[2], c.MagicCount)
	}
}

type CAnalyse struct {
	INode
	//
	CardIndex [IndexMax]int
	KindItem  KindItem
	deep      int
	jiang     bool
}

func (c *CAnalyse) Init() {
	c.deep = 0
	c.jiang = false
	if c.INode == nil {
		c.INode = &CNode{}
	}
}

// 输出指定长度链条
func (c *CAnalyse) Trace(str string, maxDeep int, deepCount int) {
	if deepCount > maxDeep || c.Count() == 0 {
		if deepCount < maxDeep {
			return
		} else {
			str = fmt.Sprintf("%s|%d|%s", str, c.deep, c.KindItem.String())
		}

		fmt.Println(str)
		return
	}

	for {
		next := c.Next()
		if next == nil {
			break
		}
		//忽略根节点
		if c.deep == 0 {
			next.(*CAnalyse).Trace(str, maxDeep, deepCount+1)
		} else {
			next.(*CAnalyse).Trace(fmt.Sprintf("%s|%d|%s", str, c.deep, c.KindItem.String()), maxDeep, deepCount+1)
		}

	}

}

// 输出每个节点
func (c *CAnalyse) Print() {
	//fmt.Println("[%d]", c.deep, c.KindItem.String())
	fmt.Println(fmt.Sprintf("(%d)%s", c.deep, c.KindItem.String()))
	for {
		next := c.Next()
		if next == nil {
			break
		}
		next.(*CAnalyse).Print()
	}
}

// 辅助函数
func (c *CAnalyse) AddKind(kind int, CardIndex [IndexMax]int, index [3]int, count [3]int, targetMagicCount int) bool {
	//检查是否满足
	if count[0]+count[1]+count[2]+targetMagicCount < 3 || targetMagicCount > CardIndex[MagicIndex] {
		return false
	}
	//
	newNode := CAnalyse{}
	newNode.Init()
	newNode.KindItem.Set(kind, targetMagicCount, index[0], index)
	newNode.deep = c.deep + 1
	newNode.jiang = c.jiang
	//将
	if kind == Jiang {
		if CardIndex[index[0]]+targetMagicCount < 2 {
			return false
		}
		newNode.CardIndex = CardIndex
		newNode.CardIndex[MagicIndex] -= targetMagicCount
		newNode.CardIndex[index[0]] -= 2 - targetMagicCount
		newNode.jiang = true
		c.Add(&newNode)
		return true
	}
	//
	if targetMagicCount == 0 && count[0] > 0 && count[1] > 0 && count[2] > 0 { //0癞子
		newNode.CardIndex = CardIndex
		newNode.CardIndex[index[0]]--
		newNode.CardIndex[index[1]]--
		newNode.CardIndex[index[2]]--
		if newNode.CardIndex[index[2]] < 0 { //坎
			return false
		}
		c.Add(&newNode)
		return true

	} else if CardIndex[MagicIndex] >= targetMagicCount {
		if targetMagicCount == 1 { //1个癞子
			newNode.CardIndex = CardIndex
			newNode.CardIndex[MagicIndex] -= targetMagicCount
			//
			if index[0] == index[1] { //坎
				newNode.CardIndex[index[0]] -= 2
				if newNode.CardIndex[index[0]] < 0 {
					return false
				}
			} else if count[1] > 0 && count[2] > 0 {
				newNode.CardIndex[index[1]]--
				newNode.CardIndex[index[2]]--
			} else if count[0] > 0 && count[2] > 0 {
				newNode.CardIndex[index[0]]--
				newNode.CardIndex[index[2]]--
			} else if count[0] > 0 && count[1] > 0 {
				newNode.CardIndex[index[0]]--
				newNode.CardIndex[index[1]]--
			} else {
				return false
			}
			c.Add(&newNode)
			return true

		} else if targetMagicCount == 2 && (count[0] > 0 || count[1] > 0 || count[2] > 0) { //2个癞子
			newNode.CardIndex = CardIndex
			newNode.CardIndex[MagicIndex] -= targetMagicCount
			if count[0] > 0 {
				newNode.CardIndex[index[0]]--
			} else if count[1] > 0 {
				newNode.CardIndex[index[1]]--
			} else if count[2] > 0 {
				newNode.CardIndex[index[2]]--
			} else {
				return false
			}
			c.Add(&newNode)
			return true
		} else if targetMagicCount == 3 { //3个癞子
			newNode.CardIndex = CardIndex
			newNode.CardIndex[MagicIndex] -= targetMagicCount
			c.Add(&newNode)
			return true
		}
	}

	return false
}

// 结果分析
func (c *CAnalyse) Analyse() {
	//
	//findKan, findShun := false, false
	for i := 0; i < IndexMax; i++ {
		if i == MagicIndex {
			continue
		}
		//坎   0~2癞子
		if c.CardIndex[i] > 0 && c.CardIndex[i]+c.CardIndex[MagicIndex] >= 3 && c.CardIndex[i] > 0 {
			c.AddKind(Peng, c.CardIndex, [3]int{i, i, i}, [3]int{c.CardIndex[i], c.CardIndex[i], c.CardIndex[i]}, 0)
			c.AddKind(Peng, c.CardIndex, [3]int{i, i, i}, [3]int{c.CardIndex[i], c.CardIndex[i], c.CardIndex[i]}, 1)
			c.AddKind(Peng, c.CardIndex, [3]int{i, i, i}, [3]int{c.CardIndex[i], c.CardIndex[i], c.CardIndex[i]}, 2)
		}
		//顺子(7 - -) 0~2癞子
		if i%9 < 7 && i < TongMax && (c.CardIndex[i]+c.CardIndex[i+1]+c.CardIndex[i+2]+c.CardIndex[MagicIndex]) >= 3 && c.CardIndex[i] > 0 {
			c.AddKind(LeftChi, c.CardIndex, [3]int{i, i + 1, i + 2}, [3]int{c.CardIndex[i], c.CardIndex[i+1], c.CardIndex[i+2]}, 0)
			c.AddKind(LeftChi, c.CardIndex, [3]int{i, i + 1, i + 2}, [3]int{c.CardIndex[i], c.CardIndex[i+1], c.CardIndex[i+2]}, 1)
			c.AddKind(LeftChi, c.CardIndex, [3]int{i, i + 1, i + 2}, [3]int{c.CardIndex[i], c.CardIndex[i+1], c.CardIndex[i+2]}, 2)
		}
		//顺子(- 8 -) 0~2癞子
		if i%9 == 7 && i < TongMax && (c.CardIndex[i-1]+c.CardIndex[i]+c.CardIndex[i+1]+c.CardIndex[MagicIndex]) >= 3 && c.CardIndex[i] > 0 {
			c.AddKind(CenterChi, c.CardIndex, [3]int{i - 1, i, i + 1}, [3]int{c.CardIndex[i-1], c.CardIndex[i], c.CardIndex[i+1]}, 0)
			c.AddKind(CenterChi, c.CardIndex, [3]int{i - 1, i, i + 1}, [3]int{c.CardIndex[i-1], c.CardIndex[i], c.CardIndex[i+1]}, 1)
			c.AddKind(CenterChi, c.CardIndex, [3]int{i - 1, i, i + 1}, [3]int{c.CardIndex[i-1], c.CardIndex[i], c.CardIndex[i+1]}, 2)
		}
		//顺子(- - 9) 0~2癞子
		if i%9 == 8 && i < TongMax && (c.CardIndex[i-2]+c.CardIndex[i-1]+c.CardIndex[i]+c.CardIndex[MagicIndex]) >= 3 && c.CardIndex[i] > 0 {
			c.AddKind(RightChi, c.CardIndex, [3]int{i - 2, i - 1, i}, [3]int{c.CardIndex[i-2], c.CardIndex[i-1], c.CardIndex[i]}, 0)
			c.AddKind(RightChi, c.CardIndex, [3]int{i - 2, i - 1, i}, [3]int{c.CardIndex[i-2], c.CardIndex[i-1], c.CardIndex[i]}, 1)
			c.AddKind(RightChi, c.CardIndex, [3]int{i - 2, i - 1, i}, [3]int{c.CardIndex[i-2], c.CardIndex[i-1], c.CardIndex[i]}, 2)
		}
		//将 0~1癞子
		if !c.jiang && c.CardIndex[i]+c.CardIndex[MagicIndex] >= 2 && c.CardIndex[i] > 0 {
			c.AddKind(Jiang, c.CardIndex, [3]int{i, i, 0}, [3]int{c.CardIndex[i], c.CardIndex[i], 0}, 0)
			c.AddKind(Jiang, c.CardIndex, [3]int{i, i, 0}, [3]int{c.CardIndex[i], c.CardIndex[i], 0}, 1)
		}
		if c.Count() > 0 {
			break
		}
	}
	//
	if c.Count() == 0 {
		if c.CardIndex[MagicIndex] >= 3 { //纯癞子坎
			//
			c.AddKind(Peng, c.CardIndex, [3]int{0, 0, 0}, [3]int{0, 0, 0}, 3)

		}
	}

	//
	for {
		next := c.Next()
		if next == nil {
			break
		}
		next.(*CAnalyse).Analyse()
	}
}

func main() {
	tmStart := time.Now().UnixMilli()
	/*
		0~8: 万
		9~17: 条
		18~26: 筒
		27~34: 风,东南西北中发白
		效率(万次):
		1癞子:400ms
		2癞子:2000ms
		3癞子:2000ms
		4癞子:2500ms
		5癞子:3500ms
		6癞子:4500ms
		7癞子:5500ms
		8癞子:6500ms
		9癞子:3000ms
		10癞子:1800ms
	*/
	input := [IndexMax]int{
		1, 0, 0, 0, 0, 0, 0, 0, 0,
		1, 0, 0, 0, 0, 0, 0, 0, 1,
		1, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 10, 0, 0,
	}
	//
	for i := 0; i < 10000; i++ {
		game := CAnalyse{}
		game.Init()
		game.CardIndex = input
		game.Analyse()
		//
		//game.Trace("", 5, 0)
		//结果示例:
		//|1|[0 0 0(0)]|2|[9 10 11(0)]|3|[15 16 17(0)]|4|[18 19 20(1)]|5|[26 26 -(0)]
	}
	//game.Print()
	//
	tmEnd := time.Now().UnixMilli()
	fmt.Printf(fmt.Sprintf("耗时：%d毫秒，结果:%d\n", tmEnd-tmStart, len(input)))
}
