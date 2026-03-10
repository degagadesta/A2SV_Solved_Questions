class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp = []
        for i in range(len(position)) :
            temp.append([position[i], speed[i]])   
        temp.sort(reverse = True)
        st = []
        for i in temp :
            time = (target - i[0]) / i[1]   
            if not  st or time > st[-1]  :
                st.append(time)
        return  len(st)          


            