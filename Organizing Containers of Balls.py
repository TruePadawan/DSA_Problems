def organizingContainers(container):
    container_sizes = []
    ball_types = [0] * len(container)

    for row in container:
        container_size = 0
        for i in range(len(row)):
            container_size += row[i]
            ball_types[i] += row[i]
        container_sizes.append(container_size)
    container_sizes.sort()
    ball_types.sort()
    print(ball_types, container_sizes)
    return "Possible" if container_sizes == ball_types else "Impossible"

a = [1,2,3]
b = [1,3,2]
print(a == b)