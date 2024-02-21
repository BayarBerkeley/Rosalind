def sorting_by_reversals2(perm):
    """
    Perform sorting by reversals using a 2-approximation algorithm.

    Args:
    perm (list): A list representing a permutation.

    Returns:
    list: A sorted permutation.
    """
    def has_decreasing_strip(perm):
        """
        Check if the given permutation contains a decreasing strip.

        Args:
        perm (list): A list representing a permutation.

        Returns:
        bool: True if a decreasing strip is found, False otherwise.
        """
        for i in range(len(perm) - 1):
            if perm[i] > perm[i + 1]:
                return True
        return False

    def find_reversal(perm, decreasing_strip):
        """
        Find the reversal that reduces two breakpoints if there is no
        decreasing strip remaining after the reversal.

        Args:
        perm (list): A list representing a permutation.
        decreasing_strip (bool): Indicates whether a decreasing strip exists.

        Returns:
        list: A reversal operation.
        """
        if decreasing_strip:
            k = min(perm[i] for i in range(len(perm) - 1) if perm[i] > perm[i + 1])
            rev_point = perm.index(k)
            rev = perm[:rev_point + 2][::-1] + perm[rev_point + 2:]
            if not has_decreasing_strip(rev):
                return rev
            l = max(perm[i] for i in range(len(perm) - 1) if perm[i] > perm[i + 1])
            rev_point = perm.index(l)
            return perm[:rev_point][::-1] + perm[rev_point:]

        # If no decreasing strip exists, cut the first two breakpoints
        return perm[1::-1] + perm[2:]

    while has_decreasing_strip(perm):
        reversal = find_reversal(perm, True)
        perm = reversal
    return perm

# Example usage:
permutation = [3, 10, 8, 2, 5, 4, 7, 1, 6, 9]
sorted_permutation = sorting_by_reversals2(permutation)
print(sorted_permutation)
