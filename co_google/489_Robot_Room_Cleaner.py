#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/robot-room-cleaner/

Given a robot cleaner in a room modeled as a grid.

Each cell in the grid can be empty or blocked.

The robot cleaner with 4 given APIs can
1. move forward,
2. turn left or
3. turn right.
Each turn it made is 90 degrees.


When it tries to move into a blocked cell,
its bumper sensor detects the obstacle and it stays on the current cell.


Design an algorithm to clean the entire room using only the 4 given
APIs shown below.

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}

Example:
Input:
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
row = 1,
col = 3

Explanation:
All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.
Notes:

The input is only given to initialize the room and the robot's position internally.
(重要!)
You must solve this problem "blindfolded".

In other words, you must control the robot using only the mentioned 4 APIs,
without knowing the room layout and the initial robot's position.

The robot's initial position will always be in an accessible cell.

(重要)
The initial direction of the robot will be facing up.

All accessible cells are connected,
which means the all cells marked as 1 will be accessible by the robot.

Assume all four edges of the grid are all surrounded by wall.
"""


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
class Robot(object):
    def __init__(self):
        self.room = [
          [1,1,1,1,1,0,1,1],
          [1,1,1,1,1,0,1,1],
          [1,0,1,1,1,1,1,1],
          [0,0,0,1,0,0,0,0],
          [1,1,1,1,1,1,1,1]
        ]
        self.facing = ["W", "N", "E", "S"]
        self.row = 1
        self.col = 3
        self.crow = self.row
        self.ccol = self.col
        self.cdirect = 1
        self.dmap = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
        self.cleaned = set()

    def move(self):
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        :rtype bool
        """
        move = self.dmap[self.facing[self.cdirect]]
        nx, ny = self.crow + move[0], self.ccol + move[1]

        if not 0 <= nx < len(self.room) or not 0 <= ny < len(self.room[0]) or \
            self.roor[nx][ny] == 0:
            return False

        self.crow = nx
        self.ccol = ny
        return True

    def turnLeft(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        self.cdirect = (self.cdirect - 1) % 4

    def turnRight(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        self.cdirect = (self.cdirect + 1) % 4

    def clean(self):
        """
        Clean the current cell.
        :rtype void
        """
        self.cleaned.add((self.crow, self.ccol))


class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        cleaned = set()

        def dfs(x, y, dx, dy):
            """
            x, y: 目前要clean的slot
            dx, dy: 移動offset
            """
            # 1, Clean current
            robot.clean();
            cleaned.add((x, y))

            # 2, Clean next
            for _ in range(4):
                if (x + dx, y + dy) not in cleaned and robot.move():
                    dfs(x + dx, y + dy, dx, dy)

                robot.turnLeft()
                # smart. turnleft and dx = -dy
                dx, dy = -dy, dx

            # 3, Back to previous position and direction
            robot.turnLeft()
            robot.turnLeft()
            # ignore if visited because it must have...
            robot.move()
            robot.turnLeft()
            robot.turnLeft()

        dfs(0, 0, 0, 1)


def build():
    pass

if __name__ == "__main__":
    s = Solution()
