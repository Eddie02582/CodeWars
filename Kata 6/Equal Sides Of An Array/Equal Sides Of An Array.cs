/*

{1,2,3,4,3,2,1}: index 3 ,left {1,2,3} right {3,2,1} left sum==right sum
if sum {20,10,-80,10,10,15,35} return 0
if none return -1

*/
using System.Linq;
public class Kata
{
  //My solution
  public static int FindEvenIndex(int[] arr)
  {
    for(var i = 0; i < arr.Length; i++)
    {
      if(arr.Take(i).Sum() == arr.Skip(i+1).Sum()) { return i; }
    }
    return -1;
  }
  
  public static int FindEvenIndex(int[] arr)
    {
        int leftSum = 0, rightSum = arr.Sum();

        for (int i = 0; i < arr.Length; ++i)
        {
            rightSum -= arr[i];

            if (leftSum == rightSum)
            {
                return i;
            }

            leftSum += arr[i];
        }

        return -1;
    }
}