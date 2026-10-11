class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs1 = list(strs)
        hash_map=dict()

        for i in range(len(strs)):
            str1= strs1[i]
            str1 = sorted(str1)
            #print(str1)
            tmp = ""
            for letter in str1:
                tmp += letter
            str1 = tmp
            strs1[i]=str1
            if str1 in hash_map:
                hash_map[str1].append(i)
            else:
                hash_map[str1]=[i]

        ans = []
        #print(hash_map)
        for key in hash_map:
            curr = []
            for i in (hash_map[key]):
                curr.append(strs[i])
            ans.append(curr)
        return ans 

