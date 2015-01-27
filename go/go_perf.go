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
	var array = []int{2, 1, 4, 5, 3}
	fmt.Println(insertionSort(array))
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

// Insertion sort
func insertionSort(array []int) {
	for i := 1; i < len(array); i++ {
		for j := i; j > 0 && array[j] < array[j-1]; j-- {
			algoutils.Swap(array, j, j-1)
		}
	}
}
