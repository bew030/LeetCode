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
    </tbody>
  </table>
  
  Work on linked lists: 
  <a href = 'https://leetcode.com/tag/linked-list/'>Linked Lists</a>
