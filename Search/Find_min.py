def distance_min(heaters, houses):
    distance_all = [None] * len(houses)
    for i, target in enumerate(houses):
        left, right = 0, len(heaters) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if heaters[mid] == target:
                distance_all[i] = 0
                break
            elif heaters[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if distance_all[i] != 0:
            if heaters[left] == target or heaters[right] == target:
                distance_all[i] = 0
            elif abs(heaters[left] - target) > abs(heaters[right] - target):
                distance_all[i] = abs(heaters[right] - target)
            else:
                distance_all[i] = abs(heaters[left] - target)
    return distance_all, max(distance_all)

if __name__ == '__main__':
    houses = [1, 2, 3, 4, 5, 6, 7]
    heaters = [2, 4]
    result_all, result_final = distance_min(heaters, houses)
    print(result_all, result_final)