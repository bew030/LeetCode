# LeetCode

To Do: 
- create folders for language (prob focus on Python and Java)
- create an overall table (problem number, Problem Title, categories, language redirect, notes) 

Ex Table: 
| #        | Title           | Categories  | Solutions | Notes |
| ------------- |-------------| -----|-------------| -----|
| 1     | Two Sum | Array, Hashtable |<ul><li>Python</li><li>Java</li></ul> |<ul><li>This is a note</li></ul>|

<table>
  <thead>
    <tr>
      <th> # </th>
      <th> Title </th>
      <th> Categories </th>
      <th> Solutions </th>
      <th> Notes </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>20</td>
      <td><a href="https://leetcode.com/problems/valid-parentheses/" target="_blank"> Valid Parentheses </a></td>
      <td> Stacks </td>
      <td>        
        <ul>
          <li><a href="https://github.com/bew030/LeetCode/blob/main/Python/20-validparentheses-stack.py" target="_blank"> Python </a></li>
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
    
  </tbody>
</table>
