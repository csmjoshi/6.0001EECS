# Problem Set 4A
# Name: Mehul Joshi
# Collaborators: n/a
# Time Spent: 2hrs




def get_permutations(sequence):

        return permute_helper([ch for ch in sequence], 0, len(sequence) - 1, [])


def permute_helper(list, start, end, permutations):
        s = combineList(list)
        if s not in permutations:
                permutations.append(s)
        if len(list) == 1:
                return combineList(list)
        else:
                for i in range(start, end+1):   
                        list[start], list[i] = list[i], list[start]
                        permute_helper(list, start+1, end, permutations)
                        list[start], list[i] = list[i], list[start]
                        
                return permutations

def combineList(list):
        s=""
        for l in list:
                s+=l
        return s

   
if __name__ == '__main__':
        print("The permutations for the word lion are: ", get_permutations("lion"))

