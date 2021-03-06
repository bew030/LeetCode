# LeetCode

To Do: 
- create folders for language (prob focus on Python and Java)
- create an overall table (problem number, Problem Title, categories, language redirect, notes) 

  <table>
    <thead>
      <tr>
        <th>Number</th>
        <th>Title</th>
        <th>Category</th>
        <th>Solution</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
        <tr>
            <td>19</td>
            <td><a href="Remove Nth Node From End of List" target="_blank"> Remove Nth node from the end of a linked list </a></td>
            <td> Linked Lists, Two Pointers </td>
            <td>
              <ul>
                <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/19-removenthnodefromend-linkedlisttwopointers.py'>Python</a></li>
                <li><a>Java</a></li>
              </ul>
            </td>
            <td>
              <ul>
                <li> TL;DR: Given the head of a linked list, remove the nth node from the end of the list and return its head. </li>
                <li> I accomplished this with 4 pointers; 1 iterator pointer, 1 nth Node pointer, 1 before nth node pointer, and 1 after nth node pointer. My logic was that I'd follow along the iterator until it reached the end of the linked list. When the iterator reaches the nth node in the linked list, it'll set the nth node pointer to the beginning of the linked list (so the nth node pointer is always n nodes away from the current end, which is what the iterator is pointing at). before nth node and after nth node pointer are both set accordingly. Once the iterator reaches the end, I set the before nth nodes next value to after nth node which succesfully deletes the nth node. I also made some specific rules for when the nth node is the first item in the linked list. </li>
              </ul>
            </td>
        </tr>
        <tr>
            <td>20</td>
            <td><a href="https://leetcode.com/problems/valid-parentheses/" target="_blank"> Valid Parentheses </a></td>
            <td>Stacks</td>
            <td>
              <ul>
                <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/20-validparentheses-stack.py'>Python</a></li>
                <li><a>Java</a></li>
              </ul>
            </td>
            <td>
              <ul>
                <li> TL;DR: Given a string of brackets, determine if it's valid (open bracket is closed by the same type of bracket and must be closed in the correct order). Using a stack you can push open brackets and pop closing brackets if it's the correct bracket. If the stack is empty, the closing bracket doesn't match, or the stack has brackets left over, it's not a valid string.</li>
              </ul>
            </td>
        </tr>
        <tr>
            <td>21</td>
            <td><a href="https://leetcode.com/problems/merge-two-sorted-lists/" target="_blank"> Merge Two Sorted Lists </a></td>
            <td> Linked Lists </td>
            <td>
              <ul>
                <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/21-mergetwosortedlists-linkedlist.py'>Python</a></li>
                <li><a>Java</a></li>
              </ul>
            </td>
            <td>
              <ul>
                <li> TL;DR: Given the heads of two sorted linked lists list1 and list2, merge the two lists into one sorted list. </li>
                <li> Did really well this time! Created a third list and p3. Iterated through p1 and p2, setting p3.val to the lower val, creating a new node, setting p3.next to the new node, and then setting p3 to p3.next, we were able to ensure that p3 was always pointing to the end of the third list. </li>
              </ul>
            </td>
        </tr>
        <tr>
            <td>35</td>
            <td><a href="https://leetcode.com/problems/search-insert-position/" target="_blank"> Search Insert Position </a></td>
            <td> Binary Search</td>
            <td>
              <ul>
                <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/35-searchinsertposition-binarysearch.py'>Python</a></li>
                <li><a>Java</a></li>
              </ul>
            </td>
            <td>
              <ul>
                <li> TL;DR: Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. </li>
                <li> Very similar to the binary search problem. I also added rules if there wasn't an exact match found; if target is larger than left/right, then return left + 1. Else, return left (since the target is located on the index you left off on). </li>
              </ul>
            </td>
        </tr>
        <tr>
          <td>59</td>
          <td><a href="https://leetcode.com/problems/spiral-matrix-ii/" target="_blank"> Spiral Matrtix II </a></td>
          <td> Arrays </td>
          <td>        
            <ul>
              <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/59-spiralmatrix2-array.py'>Python</a></li>
              <li><a>Java</a></li>
            </ul>
          </td>
          <td>
            <ul>
              <li> TL;DR: Given an integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order. </li>
              <li> Pretty challenging but fun problem; I essentially made a ruleset for each direction and slowly modified it. I noticed there
              were patterns for how many times the row/column would get iterated and built a few while/for loops around it. </li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>83</td>
          <td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-list/" target="_blank"> Remove Duplicates from Sorted List </a></td>
          <td> Arrays </td>
          <td>        
            <ul>
              <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/83-removeduplicatesfromsortedlist-linkedlist.py'>Python</a></li>
              <li><a>Java</a></li>
            </ul>
          </td>
          <td>
            <ul>
              <li> TL;DR: Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well. </li>
              <li> You're getting better at linked list problems. Used the knowledge from keep m remove n in a linked list. I set an iterator to head.next and last_non_duplicate to head. While the iterator isn't none, I check to see if the iterator.val is equal to last_non_duplicate,val. If it is, then I continue iterating iterator (iterator = iterator.next); if iterator.next is None, then I set last_non_duplicate.next to None. If it isn't equal, then I set last_non_duplicate.next to the iterator, then reset last_non_duplicate to the iterator, and continue on iterating. In doing so I ensure last_non_duplicate is always a little behind iterator and is always pointing to a unique node, setting the unique nodes next node to the next unique node. </li>
            </ul>
          </td>
        </tr>
        <tr>
            <td>160</td>
            <td><a href="https://leetcode.com/problems/intersection-of-two-linked-lists/" target="_blank"> Intersection of Two Linked List </a></td>
            <td> Linked List </td>
            <td>
              <ul>
                <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/160-intersectionoftwolinkedlists-linkedlists.py'>Python</a></li>
                <li><a>Java</a></li>
              </ul>
            </td>
            <td>
              <ul>
                <li> TL;DR: Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.</li>
                <li> I implemented two solutions. <b>Solution 1:</b> calculate length of both lists, find minimum length, shorten the longest list to the
                  minimum length (keeping the LAST n nodes where n is the minimum), then loop through the unshortened list and shortened list and 
                  see if they're equal. If they both reach the end and are NOT equal, return None. This is built on the premise that if there are
                  duplicates then it must be near the end and is at most n nodes where n is the shorter length. <b> Solution 2: </b> Iterate 
                  through the first list and add each node in a set. Then iterate through the second list and check if the node is in the set. If you 
                  iterate through the entire second list and don't see any nodes, return None. There's also a 3rd solution which measures both the 
                  longer list and shorter lisdt and redirects the shorter list to the longer list, stepping through the list at the same time. I didn't
                  understand it, BUT YOU SHOULD TRY TO UNDERSTAND IT. </li>
              </ul>
            </td>
        </tr>
        <tr>
            <td>167</td>
            <td><a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/" target="_blank"> Two Sum II - Input Array Is Sorted </a></td>
            <td>Stacks</td>
            <td>
              <ul>
                <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/167-twosum2sortedarray-twopointers.py'>Python</a></li>
                <li><a>Java</a></li>
              </ul>
            </td>
            <td>
              <ul>
                <li> TL;DR: Given a 1-indexed array that's sorted in increasing order, find two numbers that add up to a specific target number. There's always exactly one solution. </li>
                <li> I made a pointer to the left of the array and right of the array. Then, while numbers[left] + numbers[right] doesn't equal the target, I check if the sum is less or more than the target. If it's less than the target, I increase left index, otherwise I decrease the right index. I keep on doing this until I find the indices of the numbers that add up to the target and return left + 1, right + 1. </li>
              </ul>
            </td>
        </tr>
        <tr>
            <td>189</td>
            <td><a href="https://leetcode.com/problems/rotate-array/" target="_blank"> Rotate Array </a></td>
            <td>Stacks</td>
            <td>
              <ul>
                <li><a href = '189-rotatearray-twopointer.pyy'>Python</a></li>
                <li><a>Java</a></li>
              </ul>
            </td>
            <td>
              <ul>
                <li> TL;DR: Given an array, rotate the array to the right by k steps, where k is non-negative. </li>
                <li> I made 2 solutions. 1) make a copy of the list, iterate through the list, calculate the future index (i + k)%len(nums) and then set the value accordingly. You need the copy as a reference. 2) figure out the 'beginning' of the new array (which is the last k digits of the array) and the 'end' of the new array (which is the first len(n)-k digits of the array). Then create a new result array (beginning + end) and set the original array to this new result array. </li>
              </ul>
            </td>
        </tr>
        <tr>
            <td>206</td>
            <td><a href="https://leetcode.com/problems/reverse-linked-list/" target="_blank"> Reverse Linked List </a></td>
            <td> Linked List </td>
            <td>
              <ul>
                <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/206-reverselinkedlist-linkedlist.py'>Python</a></li>
                <li><a>Java</a></li>
              </ul>
            </td>
            <td>
              <ul>
                <li> TL;DR: Given the head of a singly linked list, reverse the list, and return the reversed list.</li>
                <li> I did it by having a pointer to the previous node, current node, and next node. I'd set the current node to the previous node, setting the previous node to the current node (which now has the current node and the previous nodes), setting the current node to the next node, and setting the next node to the next next node. View visual explanation <a href = "https://github.com/bew030/LeetCode/blob/main/image%20references/IMG_BC503F233A2F-1.jpeg"> here</a>. </li>
              </ul>
            </td>
        </tr>
        <tr>
          <td>232</td>
          <td><a href="https://leetcode.com/problems/implement-queue-using-stacks/" target="_blank"> Implement Qeueue using Stacks </a></td>
          <td> Stacks, Queues </td>
          <td>        
            <ul>
              <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/232-queuewstacks-stackqueue.py'>Python</a></li>
              <li><a>Java</a></li>
            </ul>
          </td>
          <td>
            <ul>
              <li> TL;DR: Use two stacks to implement the FIFO concept. Empty current queue into storage queue, add new item, and then pop the storage queue back into the current queue. That way the first item remains at the top. </li>
              <li> It seems like Java is a little better for this, in Python you use lists for the stacks. </li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>237</td>
          <td><a href="https://leetcode.com/problems/delete-node-in-a-linked-list/" target="_blank"> Delete Node in a Linked List </a></td>
          <td> Linked List </td>
          <td>        
            <ul>
              <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/237-deletenodeinlinkedlist-linkedlist.py'>Python</a></li>
              <li><a>Java</a></li>
            </ul>
          </td>
          <td>
            <ul>
              <li> TL;DR: Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly. </li>
              <li> I basically just changed the nodes value and nodes next variable. I did it by setting node.val to node.next.val and then node.next to node.next.next, effectively 'deleting' (or better described as setting it as the next node) the node. </li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>278</td>
          <td><a href="https://leetcode.com/problems/first-bad-version/" target="_blank"> First Bad Version </a></td>
          <td> Binary Search </td>
          <td>        
            <ul>
              <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/278-firstbadversion-binarysearch.py'>Python</a></li>
              <li><a>Java</a></li>
            </ul>
          </td>
          <td>
            <ul>
              <li> TL;DR: You're given a bunch of versions of a product and you have to find out when the first version is that went bad. If the version went bad, all following versions are bad. </li>
              <li> Use a binary search; if you check the middle and the version is good, then you have to look at future versions, so you set left to midpt + 1. If version is bad you have to check previous versions so you set right to midpt (its not midpt - 1 since the midpt might be the first time you got a bad version). Return when left and right are the same value, signifying the first bad version. </li>
            </ul>
          </td>
        </tr>
        <tr>
            <td>283</td>
            <td><a href="https://leetcode.com/problems/move-zeroes/" target="_blank"> Move Zeroes </a></td>
            <td> Linked List </td>
            <td>
              <ul>
                <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/283-movezeroes-twopointers.py'>Python</a></li>
                <li><a>Java</a></li>
              </ul>
            </td>
            <td>
              <ul>
                <li> TL;DR: Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. Do it in place. </li>
                <li> I had a pointer pointing at the last_nonzero_index (which started off at -1). It then iterates through the array; if a number isn't 0, then I switch it with the number at the last nonzero index (the number should be zero) and increase the last_nonzero_index by 1 (so I know where to add the next non zero number). </li>
              </ul>
            </td>
        </tr>
        <tr>
          <td>289</td>
          <td><a href="https://leetcode.com/problems/game-of-life/" target="_blank"> Game of Life </a></td>
          <td> Array </td>
          <td>        
            <ul>
              <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/289-gameoflife-array.py'>Python</a></li>
              <li><a>Java</a></li>
            </ul>
          </td>
          <td>
            <ul>
              <li> TL;DR: You're given a board made of mxn cells that follow a few rules on whether the cell lives or dies (dependant on its neighbors). Return the next state of the board. </li>
              <li> I did it by iterating through the board and creating a list of neighboring values. Then I counted the neighbors and modified it in a new array. After everything was done I remodified the original board. This was technically correct, but I should try re-implementing it where it changes the original board but adds in a few states as well (dead -> alive, alive -> dead, etc.) TRY REIMPLEMENTING IT THIS WAY. </li>
            </ul>
          </td>
        </tr>
      <tr>
          <td>344</td>
          <td><a href="https://leetcode.com/problems/reverse-string/" target="_blank"> Reverse String </a></td>
          <td> Strings </td>
          <td>        
            <ul>
              <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/344-reversestring-string.py'>Python</a></li>
              <li><a>Java</a></li>
            </ul>
          </td>
          <td>
            <ul>
              <li> TL;DR: Write a function that reverses a string. The input string is given as an array of characters s. You must do this by modifying the input array in-place with O(1) extra memory. </li>
              <li> I set two pointers, one pointing to the beginning of the string and one to the end of the string. While the left is less than the right, I switch the two characters around and then iterate left up by one and right down by one. Doing so successfully reverses the string. </li>
            </ul>
          </td>
        </tr>
      <tr>
          <td>557</td>
          <td><a href="https://leetcode.com/problems/reverse-words-in-a-string-iii/" target="_blank"> Reverse Words in String 3 </a></td>
          <td> Strings </td>
          <td>        
            <ul>
              <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/557-reversewordsinstring3-string.py'>Python</a></li>
              <li><a>Java</a></li>
            </ul>
          </td>
          <td>
            <ul>
              <li> TL;DR: Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order. </li>
              <li> I split the string up by whitespaces using .split(), then reversed each word in the list using list comprehension ([::-1]), then joined the list with the .join method (' '.join(reversed_words_list)). </li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>682</td>
          <td><a href="https://leetcode.com/problems/baseball-game/" target="_blank"> Baseball Game </a></td>
          <td> Stacks, Lists </td>
          <td>        
            <ul>
              <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/682-baseballgame-arraystack.py'>Python</a></li>
              <li><a>Java</a></li>
            </ul>
          </td>
          <td>
            <ul>
              <li> TL;DR: You're given a list of characters that represent a baseball game. If it's an integer, add it to the score. If it's '+', record a score that's the sum of the two previous scores. if it's a 'D', add double the previous score. If it's 'C', remove the previous score. You can do this using stacks or list manipulation, iterating through the list once. Once you've gotten a score list return the sum. </li>
              <li> Remember to think about the negative number edge case next time (can't just use .isdigit() on a negative number) </li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>704</td>
          <td><a href="https://leetcode.com/problems/binary-search/" target="_blank"> Binary Search </a></td>
          <td> Binary Search </td>
          <td>        
            <ul>
              <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/704-binarysearch-binarysearch.py'>Python</a></li>
              <li><a>Java</a></li>
            </ul>
          </td>
          <td>
            <ul>
              <li> TL;DR: Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1. </li>
              <li> Implement left as 0 and right as len(nums) - 1. If midpt (which is left + (right - left)//2) is less than target, then target is potentially on the right side, so you shift left to midpt + 1. If target is more than target, target is potentially on the left side, so you shift right to midpt - 1. Keep on going until either midpt is target or until left !< right. If midpt doesnt equal target, return -1. </li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>876</td>
          <td><a href="https://leetcode.com/problems/middle-of-the-linked-list/" target="_blank"> Middle of the Linked List </a></td>
          <td> Linked List, Two Pointers </td>
          <td>        
            <ul>
              <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/876-middleoflinkedlist-linkedlisttwopointer.py'>Python</a></li>
              <li><a>Java</a></li>
            </ul>
          </td>
          <td>
            <ul>
              <li> TL;DR: Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node. </li>
              <li> Initially I did it the naive way where I just counted the length, then reitterated through the linked list and return the node at length//2. A better solution would be to just store each node into an array and return array[len(array)//2], saving on run time. An even better way would be to implement fast/slow pointers and return the slow pointer whenever the fast pointer reached the end (assuming the fast pointer is twice as fast).  </li>
              <li> 2nd attempt update: was able to successfully do the two pointer method. Note that the faster pointer is continuing until it is either the last node or past the last node; therefore the while loop should be 'while fast_pointer and fast_pointer.next:' </li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>977</td>
          <td><a href="https://leetcode.com/problems/squares-of-a-sorted-array/" target="_blank"> Middle of the Linked List </a></td>
          <td> Linked List, Two Pointers </td>
          <td>        
            <ul>
              <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/977-squaresofsortedarray-twopointer.py'>Python</a></li>
              <li><a>Java</a></li>
            </ul>
          </td>
          <td>
            <ul>
              <li> TL;DR: Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order. </li>
              <li> Easy solution: square each number using list comprehension and then sort using built in list sort method. Better solution: you're comparing negative squares and positive squares, and technically the negative side is organized descending while the positive numbers are organized ascending. You can now create a left pointer and right pointer and instead build the list from greatest to smallest (since you know nums[0] or nums[-1] will be the largest value). What I do is compare the absolute value of the left number and the right value; if the abs of the left is less than the abs of the right, I select the right value, square it, add it to the end of the list, and then decrease the right index. If it's not then I select the left value, square it, add it to the end of the list, and increase the left value. I do this for the entirety of the array and return the list, thus leading to a time and space complexity of O(N)  </li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>1213</td>
          <td><a href="https://leetcode.com/problems/intersection-of-three-sorted-arrays/" target="_blank"> CIntersection of Three Sorted Arrays </a></td>
          <td> Array, Binary Search</td>
          <td>        
            <ul>
              <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/1213-intersectionofthreesortedarrays.py'>Python</a></li>
              <li><a>Java</a></li>
            </ul>
          </td>
          <td>
            <ul>
              <li> TL;DR: Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays. </li>
              <li> Two ways to do this: 1) convert all the arrays to sets, use set unions, and return a sorted list 2) use 3 pointers, iterate through the arrays if the value at the pointer is the minimum out of the 3 arrays, append to a return list if values at all 3 pointers are the same, stop when any of the pointers reach the end of their respective array, return return list. </li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>1260</td>
          <td><a href="https://leetcode.com/problems/shift-2d-grid/" target="_blank"> Shift 2D Grid </a></td>
          <td> Arrays </td>
          <td>        
            <ul>
              <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/1260-shift2dgrid-array'>Python</a></li>
              <li><a>Java</a></li>
            </ul>
          </td>
          <td>
            <ul>
              <li> TL;DR: You're given a 2D matrix and an integer k. Shift the grid k times (assuming the 2D matrix is cyclical). </li>
              <li> This was good practice for math operations (%, //). You did this pretty slowly (~20 min) so try to practice these math operations. I did it by recording the number and index, reorganizing the index based off of the shifts, and then remade the matrix by index. See if you can do it by recycling the matrix (instead of making a new one). </li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>1290</td>
          <td><a href="https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/" target="_blank"> Convert Binary Number in a Linked List to int </a></td>
          <td> Linked Lists, Bitwise Operation </td>
          <td>        
            <ul>
              <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/1290-convertbinarylinkedlist-linkedlistbinary'>Python</a></li>
              <li><a>Java</a></li>
            </ul>
          </td>
          <td>
            <ul>
              <li> TL;DR: You're given a linked list where the value is either 0 or 1. Return the decimal value of the number in the linked list. </li>
              <li> I did this by iterating through the linked list and saving it in a list, then iterating through the list and converting it to int and adding the values together. It's faster to do it by bitwise operations which I don't know. Learn it and try to reimplement it. </li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>1351</td>
          <td><a href="https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/" target="_blank"> Count Negative Numbers in a Sorted Matrix </a></td>
          <td> Binary Search </td>
          <td>        
            <ul>
              <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/1351-countnegativenumbersinsortedarray-binarysearch.py'>Python</a></li>
              <li><a>Java</a></li>
            </ul>
          </td>
          <td>
            <ul>
              <li> TL;DR: Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid. </li>
              <li> Implemented both list iteration and binary search which worked really well. If you check the bottom right number, if it's not negative, there will be no negative numbers (since that value is the lowest in the array). Knowing that, I do a list iteration from the last row and move up; in each row, I then use a binary search to find out how many negative items are in a row. If the middle item is a negative value, everything to the right of it is negative, so you can set the right to be the left of the middle. Otherwise, set the left to the right of the middle (to get the right half). I continue doing these binary searches for each row until the last value of the row isn't a negative number, in which case I stop.  </li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>1474</td>
          <td><a href="https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/" target="_blank"> Delete N Nodes after M Nodes of a Linked List </a></td>
          <td> Linked Lists </td>
          <td>        
            <ul>
              <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/1474-deletennodesaftermnodes-linkedlist.py'>Python</a></li>
              <li><a>Java</a></li>
            </ul>
          </td>
          <td>
            <ul>
              <li> TL;DR: You're given a linked list. Keep the first m nodes and remove the next n nodes; keep on doing that until you reach the end of the list. </li>
              <li> You really need to work on iterating through linked lists. Try to understand specifically what the variable is referencing (is it making a copy or is it referencing?) I think your logic is there but your references are fuzzy. REWORK THIS. EDIT: It makes more sense now, sometimes you're making a hard copy of the reference. </li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>2089</td>
          <td><a href="https://leetcode.com/problems/find-target-indices-after-sorting-array/" target="_blank"> Find Target Indices After Sorting Array </a></td>
          <td> Binary Search </td>
          <td>        
            <ul>
              <li><a href = 'https://github.com/bew030/LeetCode/blob/main/Python/2089-findtargetindicesaftersortingarray-arraybinarysearch.py'>Python</a></li>
              <li><a>Java</a></li>
            </ul>
          </td>
          <td>
            <ul>
              <li> TL;DR: Given a list, sort it and return a list of the indices of the list where the number at the indices equal a target number. </li>
              <li> Sorted by the default sort() method and then iterated through the list until either the target is found or the item at indice i is greater than target, in which case the iteration stops. IMPLEMENT IT USING BINARY SEARCH; should be faster. What do you do if it hit the target? Then you have to try both left or right? Try to figure it out. </li>
            </ul>
          </td>
        </tr>
    </tbody>
  </table>
  
  Work on linked lists: 
  <a href = 'https://leetcode.com/tag/linked-list/'>Linked Lists</a>
  
  Word on Binary Search: 
  <a href = 'https://leetcode.com/tag/binary-search/'>Binary Search</a>
