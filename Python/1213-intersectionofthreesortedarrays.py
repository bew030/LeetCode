class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        p1 = 0 
        p2 = 0 
        p3 = 0 
        
        
        return_list = []
        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3): 
            if arr1[p1] == arr2[p2] == arr3[p3]: 
                return_list.append(arr1[p1])
                p1 += 1 
                p2 += 1 
                p3 += 1 
            else: 
                min_num = min(arr1[p1], arr2[p2], arr3[p3])
                if arr1[p1] == min_num: 
                    p1 += 1 
                if arr2[p2] == min_num:
                    p2 += 1 
                if arr3[p3] == min_num: 
                    p3 += 1 
        return return_list

        '''
        return_list = list(set(arr1) & set(arr2) & set(arr3))
        return_list.sort()
        return return_list
        '''