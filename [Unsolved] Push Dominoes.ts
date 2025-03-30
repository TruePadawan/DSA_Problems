/*
* Loop through the string until an upright domino is encountered
* the domino falls left if there is a domino after it, and it is falling left
* the domino falls right if there is a previous domino, and it is falling right
* The domino stays the same if there are dominos of its left and right and they are falling in different directions
* */
function pushDominoes(dominoes: string): string {
    const LEFT = "L"
    const RIGHT = "R"
    const UPRIGHT = "."
    let firstPassResult = ""
    for (let i = 0; i < dominoes.length; i++) {
        const currentDomino = dominoes[i]
        if (currentDomino == UPRIGHT) {
            const hasNextDomino = i < dominoes.length - 1
            const hasPreviousDomino = i > 0
            const hasAdjacentDominoes = hasPreviousDomino && hasNextDomino

            const nextDomino = dominoes[i + 1]
            const previousDomino = firstPassResult[i - 1]
            const fallingInDifferentDirections = (nextDomino != UPRIGHT && previousDomino != UPRIGHT && nextDomino != previousDomino)
            if (hasAdjacentDominoes && fallingInDifferentDirections) {
                firstPassResult += UPRIGHT
            } else if (hasNextDomino && nextDomino == LEFT) {
                firstPassResult += LEFT
            } else if (hasPreviousDomino && previousDomino == RIGHT) {
                firstPassResult += RIGHT
            } else {
                firstPassResult += UPRIGHT
            }
        } else {
            firstPassResult += currentDomino
        }
    }

    let finalResult = ""
    for (let i = 0; i < dominoes.length; i++) {
        const currentDomino = firstPassResult[i]
        if (currentDomino == UPRIGHT) {
            const hasNextDomino = i < firstPassResult.length - 1
            const hasPreviousDomino = i > 0
            const hasAdjacentDominoes = hasPreviousDomino && hasNextDomino

            const nextDomino = firstPassResult[i + 1]
            const previousDomino = firstPassResult[i - 1]
            const fallingInDifferentDirections = (nextDomino != UPRIGHT && previousDomino != UPRIGHT && nextDomino != previousDomino)
            if (hasAdjacentDominoes && fallingInDifferentDirections) {
                finalResult += UPRIGHT
            } else if (hasNextDomino && nextDomino == LEFT) {
                finalResult += LEFT
            } else if (hasPreviousDomino && previousDomino == RIGHT) {
                finalResult += RIGHT
            } else {
                finalResult += UPRIGHT
            }
        } else {
            finalResult += currentDomino
        }
    }
    return finalResult
}