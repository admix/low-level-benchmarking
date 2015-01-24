// Low level performance benchmarking using Go
package main

import (
	"fmt";
	"time";
)

func main() {
	fmt.Println("Low level performance using Go")
	t := time.Now()
	regularArray(1000000)
	s := time.Now()
	fmt.Println("Time spent: %v", s.Sub(t))
}

func regularArray(maxNum int) int{
	var j int

	var Data = make([]bool,maxNum+1)
	// var Data [maxNum + 1]bool;
	for i := 2; i <= maxNum; i++ {
		Data[i] = true
	}

	for i := 2;i <= maxNum; i++ {
		if Data[i] {
			for j = i + i; j <= maxNum; j += i {
				Data[j] = false
			}
		}
	}
	return 0
}