
def main():
    print("Test")

    with open("D:\\Sandbox\AdventCode\Day4\input2.txt") as file:
        lines = [line.strip() for line in file]

    score_list = []
    for line in lines:
        score = 0
        number_sets = line.split(':')[1]
        nums = number_sets.strip().split('|')
        win_num = nums[0].strip().split(' ')
        win_num = list(filter(None, win_num))
        own_num = nums[1].strip().split(' ')
        own_num = list(filter(None, own_num))
        for i in own_num:
            if i in win_num:
                if score == 0:
                    score = 1
                else:
                    score = score*2
            # print(score) 
        score_list.append(score)
    
    print(sum(score_list))

        # print(line.split(':')[1])



   
if __name__ == "__main__":
    main()