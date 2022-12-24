import java.util.ArrayList;

public class Programmers_120893 {
    public static void main(String[] args) {
        Programmers_120893 s = new Programmers_120893();

        String my_string = "cccCCC";

        System.out.println(s.solution(my_string));
    }

    public String solution(String my_string) {
        String answer = "";

        for (String myStr : my_string.split("")) {
            if (Character.isUpperCase(myStr.charAt(0))) {
                answer += Character.toLowerCase(myStr.charAt(0));
            } else {
                answer += Character.toUpperCase(myStr.charAt(0));
            }
        }

        return answer;
    }
}
