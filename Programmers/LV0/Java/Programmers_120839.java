public class Programmers_120839 {
    public static void main(String[] args) {
        Programmers_120839 s = new Programmers_120839();

        String rsp = "2";

        System.out.println(s.solution(rsp));
    }

    public String solution(String rsp) {
        String answer = "";

        for (char s : rsp.toCharArray()) {
            if (s == '2') answer += "0";
            else if (s == '0') answer += "5";
            else answer += "2";
        }

        return answer;
    }
}
