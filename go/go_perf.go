// Low level performance benchmarking using Go
package main

import (
	"fmt"
	// "testing"
)

func regularArray(maxNum int) {
	var i int = 2
	var j int

	var Data = make([]bool, maxNum+1)

	for i := 2; i <= maxNum; i++ {
		Data[i] = true
		fmt.Println(i)
	}
	i = 2
	for i; i <= maxNum; i++ {
		if Data[i] {
			for j = i + i; j <= maxNum; j += i {
				Data[j] = false
			}
		}
	}
	fmt.Println(Data)
}

func main() {
	fmt.Println("Low level performance using Go")
	// t := testing.Benchmark(regularArray(100000))
	regularArray(100000)
	// fmt.Println(t)
}