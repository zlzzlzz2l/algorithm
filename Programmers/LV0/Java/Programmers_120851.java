public class Programmers_120851 {
    public static void main(String[] args) {
        Programmers_120851 s = new Programmers_120851();

        String my_string = "1a2b3c4d123";

        System.out.println(s.solution(my_string));
    }

    public int solution(String my_string) {
        int answer = 0;

        String[] myStr = my_string.split("");

        for (int i = 0; i < myStr.length; i++) {
            if (myStr[i].matches("[0-9]")) {
                answer += Integer.parseInt(myStr[i]);
            }
        }
        return answer;
    }
}
