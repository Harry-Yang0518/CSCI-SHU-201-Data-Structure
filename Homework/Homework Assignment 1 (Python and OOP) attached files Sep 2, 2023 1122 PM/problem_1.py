def string_generator():
    chars = ['g', 'o', 'd', 't', 'a', 'c']  # Adjusted initial order
    n = len(chars)
    indices = list(range(n))
    while True:
        yield ''.join([chars[i] for i in indices])
        # Implementing the next permutation logic
        i = n - 2
        while i >= 0 and indices[i] > indices[i + 1]:
            i -= 1
        if i == -1:
            break
        j = n - 1
        while indices[j] <= indices[i]:
            j -= 1
        indices[i], indices[j] = indices[j], indices[i]
        left, right = i + 1, n - 1
        while left < right:
            indices[left], indices[right] = indices[right], indices[left]
            left += 1
            right -= 1

def main():
    cat_dog = string_generator()
    print(next(cat_dog), next(cat_dog), next(cat_dog))  # Outputs three combinations


if __name__ == '__main__':
    main()