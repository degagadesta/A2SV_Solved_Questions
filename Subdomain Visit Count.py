class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        total_cnt=defaultdict(int)
        for domain in cpdomains:
            cnt,dom=domain.split(" ")
            cnt=int(cnt)
            total_cnt[dom]+=cnt
            for i in range(len(dom)):
                if dom[i]==".":
                    total_cnt[dom[i+1:]]+=cnt
        ans=[]
        for domain in total_cnt :
            ans.append(f"{total_cnt[domain]} {domain}") 
        return ans               
        
