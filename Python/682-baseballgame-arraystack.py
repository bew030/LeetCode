class Solution:
    def calPoints(self, ops: List[str]) -> int:
        # should have double checked for NEGATIVE NUMBERS; remember to ask 
        total_score_list = [] 
        for i in ops: 
            if i.isdigit(): 
                total_score_list.append(int(i))
            elif i[0] == '-':
                total_score_list.append(int(i[1:])*-1)
            elif i == '+':
                total_score_list.append(sum(total_score_list[-2:]))
            elif i == 'C':
                total_score_list.pop()
            elif i == 'D':
                total_score_list.append(total_score_list[-1]*2)
        print(total_score_list)
        return sum(total_score_list)