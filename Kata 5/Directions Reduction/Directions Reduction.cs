public class DirReduction {
  
    public static string[] dirReduc(String[] arr) {
         // "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" 
            Dictionary<string, string> dic = new Dictionary<string, string>();
            dic.Add("NORTH", "SOUTH");
            dic.Add("SOUTH", "NORTH");
            dic.Add("WEST", "EAST");
            dic.Add("EAST", "WEST");

            Stack<string> result = new Stack<string>();           

            foreach (string dire in arr)
            {
                if (result.Count > 0 && result.Peek() == dic[dire])                
                    result.Pop();              
                else
                    result.Push(dire);
            }
            
            return result.Reverse().ToArray();
    }
    public static string[] dirReduc2(String[] arr) {
        Dictionary<string, string> dic = new Dictionary<string, string>();
        dic.Add("NORTH", "SOUTH");
        dic.Add("SOUTH", "NORTH");
        dic.Add("WEST", "EAST");
        dic.Add("EAST", "WEST");
        
        List<string> result = new List<string>();

        foreach (string dire in arr)
        {
            if (result.Count > 0 && result[result.Count - 1] == dic[dire])
            {
                 result.RemoveAt(result.Count - 1);
            }
             else
                result.Add(dire);

        }
        return result.ToArray();

     }
}