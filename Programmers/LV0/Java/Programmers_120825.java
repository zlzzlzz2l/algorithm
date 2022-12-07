public class Programmers_120825 {
    public static void main(String[] args) {
        Programmers_120825 s = new Programmers_120825();

        String my_string = "hello";
        int n = 3;

        System.out.println(s.solution(my_string, 3));
    }

    public String solution(String my_string, int n) {
        String answer = "";

        String[] my_str = my_string.split("");

        for (String s : my_str) {
            for (int i = 0; i < n; i++) {
                answer += s;
            }
        }

        return answer;
    }
}
