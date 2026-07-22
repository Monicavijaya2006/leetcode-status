class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Max bits
        L = len(bin(max(nums))) - 2 # Ex: 13 = '0b1101'

        trie = {}
        max_xor = 0
        for num in nums:
            node = trie
            xor_node = trie
            curr_xor = 0
            left_most_mask = 1 << (L-1)
            for k in range(L):
                # get the leftmost bit
                if num & left_most_mask > 0:
                    bit = 1
                else:
                    bit = 0
                # prepare mask for next bit / iteration
                left_most_mask = left_most_mask >> 1

                # build trie
                if bit not in node:
                    node[bit] = {}
                node = node[bit]

                # compute curr_xor
                toggle_bit = 1 - bit
                if toggle_bit in xor_node:
                    curr_xor = (curr_xor << 1) | 1
                    xor_node = xor_node[toggle_bit]
                else:
                    curr_xor = curr_xor << 1
                    xor_node = xor_node[bit]

            max_xor = max(max_xor, curr_xor)
        return max_xor