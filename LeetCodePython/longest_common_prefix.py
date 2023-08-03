class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""

        min_len = min([len(s) for s in strs])

        for idx, ch_i in enumerate(strs[0][:min_len]):
            if all(s_j[idx] == ch_i for s_j in strs[1:]):
                common_prefix += ch_i
            else:
                break
        return common_prefix
