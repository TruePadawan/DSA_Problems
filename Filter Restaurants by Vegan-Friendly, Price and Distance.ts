// restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]

function filterRestaurants(restaurants: number[][], veganFriendly: number, maxPrice: number, maxDistance: number): number[] {
    // const filteredRestaurants = veganFriendly === 1 ? restaurants.filter(value => value[2] === 1) : restaurants
    const filteredRestaurants: number[][] = []
    for (const restaurant of restaurants) {
        //     Ignore all restaurants that don't meet the veganFriendly, maxPrice and maxDistance filter
        const onlyVeganFriendlyRestaurants = veganFriendly == 1 && restaurant[2] == 1
        if (onlyVeganFriendlyRestaurants || veganFriendly != 1) {
            const withinMaxPriceAndDistance = restaurant[3] <= maxPrice && restaurant[4] <= maxDistance
            if (withinMaxPriceAndDistance) {
                filteredRestaurants.push(restaurant)
            }
        }
    }
    filteredRestaurants.sort((res1, res2) => {
        const hasSameRating = res1[1] == res2[1]
        if (hasSameRating) {
            return (res1[0] < res2[0]) ? -1 : 1
        }
        return (res1[1] < res2[1]) ? -1 : 1
    }).reverse()
    const filteredIDs: number[] = filteredRestaurants.map(restaurant => restaurant[0])
    return filteredIDs
};

const res = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
console.log(filterRestaurants(res, 1, 50, 10))