using System.Linq;
public class Kata
{
    public static string TitleCase(string title, string minorWords = "")
    {

        if (title == string.Empty)
            return "";
        //*****¥i¥H¨¾¤î minorWords==null
        var minWords = (minorWords ?? "").Split(' ').Select(w => w.ToLower());
        var q = title.ToLower().Split(' ').Select((x, i) => (minWords.Contains(x) && i != 0) ? x: x.Substring(0, 1).ToUpper() + x.Substring(1));
        return string.Join(" ", q);
    }	
}