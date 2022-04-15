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
                <li> Very similar to the binary search problem. I also added rules if there wasn't an exact match found; if target is larger than left/right, then return left + 1. Else, return left (since the target is located on the index you left off on).
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
    </tbody>
  </table>
  
  Work on linked lists: 
  <a href = 'https://leetcode.com/tag/linked-list/'>Linked Lists</a>
