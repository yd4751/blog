package main

type INode interface {
	Add(node INode)
	//
	Delete(node INode)
	//
	Count() int
	//
	Get(index int) INode
	//返回下一个节点，自动循环，访问到最后一个节点后，再次调用返回nil(此时状态重置)
	Next() INode
}

type CNode struct {
	childs []INode
	pos    int
}

func (c *CNode) Add(node INode) {
	c.childs = append(c.childs, node)
}
func (c *CNode) Delete(node INode) {
	for i, v := range c.childs {
		if v == node {
			c.childs = append(c.childs[:i], c.childs[i+1:]...)
			return
		}
	}
}
func (c *CNode) Count() int {
	return len(c.childs)
}

func (c *CNode) Get(index int) INode {
	return c.childs[index]
}

func (c *CNode) Next() (next INode) {
	if c.pos < len(c.childs) {
		next = c.childs[c.pos]
		c.pos++
		return next
	}
	//重置
	c.pos = 0
	return nil
}

func init() {

}
