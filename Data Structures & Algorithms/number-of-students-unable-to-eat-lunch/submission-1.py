class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 1，1，0，0，1  | 0,0,0,1,1 unmatch = 1
        # 10011 | 00011 unmatch = 2
        # 00111 | 00011 unmatch = 0
        # 0111 | 0011 unmatch = 0
        # 111 | 011 unmatch = 1, unmatch = 2, unmatch = 3
        # then by rearranging all students in the queue and still unable to remove the sandwich at the top,
        # we know that the remaining students are unable to eat.
        # students is a queue, and sandwiches is a stack, where 0 is the top index
        unmatch = 0
        while students and sandwiches:
            if students[0] == sandwiches[0]:
                unmatch = 0
                students.pop(0)
                sandwiches.pop(0)
            else:
                unmatch += 1
                # we have rotated the entire queue and couldnt find 
                # a student that wants the top sandwich, so all of them cannot eat.
                if unmatch == len(students):
                    break
                # otherwise we deque the current top student and enque him/her
                stu = students.pop(0)
                students.append(stu)
        return unmatch