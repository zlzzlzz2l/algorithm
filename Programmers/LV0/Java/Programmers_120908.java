public class Programmers_120908 {
    public static void main(String[] args) {
        Programmers_120908 s = new Programmers_120908();

        String str1 = "ppprrrogrammers";
        String str2 = "pppp";

        System.out.println(s.solution(str1, str2));
    }

    public int solution(String str1, String str2) {
        int answer = 0;

        if (str1.contains(str2)) {
            answer += 1;
        } else answer += 2;

        return answer;
    }
}
