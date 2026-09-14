class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        l=0

        if n1>n2:
            return False

        s1_dict={}
        s2_dict={}

        for i in range(n1):
            s1_dict[s1[i]]=s1_dict.get(s1[i],0)+1
            s2_dict[s2[i]]=s2_dict.get(s2[i],0)+1
        if s1_dict==s2_dict:
            return True

        for r in range(n1,n2):
            s2_dict[s2[r]]=s2_dict.get(s2[r],0)+1
            s2_dict[s2[l]]-=1
            if s2_dict[s2[l]]==0:
                del s2_dict[s2[l]]
            l+=1
            if s1_dict==s2_dict:
                return True
        return False

