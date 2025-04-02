/*
* Loop through the questions
* At each question, check if we have the result of following the path without skipping
* If we do; If its higher than the current max sum, set max sum to it
* If we don't:
*   go through the question path and store its result
*
* */

// [[1,1],[2,2],[3,3],[4,4],[5,5]]

function mostPoints(questions: number[][]): number {
    let maxSum = 0
    if (questions.length === 0) {
        return maxSum
    }
    for (let i = 0; i < questions.length; i++) {
        const point = questions[i][0]
        const skipCount = i + questions[i][1] + 1
        const sum =  point + mostPoints(questions.slice(skipCount))
        if (sum > maxSum) {
            maxSum = sum
        }
    }
    return maxSum
}

mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])