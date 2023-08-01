class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m_pos = {}
        max_dist = 0
        id_norep = 0

        for idx, s_ in enumerate(s):
            if s_ in m_pos:
                id_previous = m_pos[s_]
                if id_norep <= id_previous:
                    id_norep =  id_previous + 1

            dist = idx - id_norep + 1
                
            max_dist = dist if dist > max_dist else max_dist
            m_pos[s_] = idx

        return max_dist
