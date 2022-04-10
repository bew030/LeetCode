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
    </tbody>
  </table>
