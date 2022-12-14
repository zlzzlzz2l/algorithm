public class Programmers_120822 {
    public static void main(String[] args) {
        Programmers_120822 s = new Programmers_120822();

        String my_string = "jaron";

        System.out.println(s.solution(my_string));
    }

    public String solution(String my_string) {
        String answer = "";
        String[] myStr = my_string.split("");

        for (int i = myStr.length - 1; i > -1 ; i--) {
            answer += myStr[i];
        }

        return answer;
    }
}
