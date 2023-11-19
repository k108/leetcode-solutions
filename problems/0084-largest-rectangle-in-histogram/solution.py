class Solution:
		def largestRectangleArea(self, heights: List[int]) -> int:
				stack=[]
				i = 0
				max_area = 0
				while i < len(heights):
					if stack == [] or heights[i]>heights[stack[-1]]:
						stack.append(i)
					else:
						curr = stack.pop()
						width = i if stack == [] else i - stack[-1]-1
						max_area = max(max_area, width*heights[curr])
						i-=1
					i+=1
				while stack != []:
					curr = stack.pop()
					width = i if stack == [] else i - stack[-1]-1
					max_area = max(max_area, width*heights[curr])
				return max_area
        
