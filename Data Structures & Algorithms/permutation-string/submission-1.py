class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count_s1 = [0] * 26
        count_s2 = [0] * 26

        for i in range(len(s1)):
            count_s1[ord(s1[i]) - 97] += 1
            count_s2[ord(s2[i]) - 97] += 1

        matches = sum(count_s1[i] == count_s2[i] for i in range(26))

        for i in range(len(s1), len(s2)):
            if matches == 26: return True

            # Add new char
            add = ord(s2[i]) - 97
            count_s2[add] += 1
            if count_s2[add] == count_s1[add]:
                matches += 1
            elif count_s2[add] == count_s1[add] + 1:
                matches -= 1

            # Remove old char
            rem = ord(s2[i - len(s1)]) - 97
            count_s2[rem] -= 1
            if count_s2[rem] == count_s1[rem]:
                matches += 1
            elif count_s2[rem] == count_s1[rem] - 1:
                matches -= 1
        return matches == 26