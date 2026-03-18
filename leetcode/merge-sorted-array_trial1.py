class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        end_1 = m-1
        end_2 = n-1
        end_all = m+n-1

        while end_2 >= 0 : 
            if end_1 >= 0 and nums1[end_1] > nums2[end_2] : 
                nums1[end_all] = nums1[end_1]

                end_1 -= 1

            else : 
                nums1[end_all] = nums2[end_2]
                end_2 -= 1

            end_all -= 1
        
        
        