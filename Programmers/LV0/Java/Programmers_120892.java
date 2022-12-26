public class Programmers_120892 {
    public static void main(String[] args) {
        Programmers_120892 s = new Programmers_120892();

        String ciper = "dfjardstddetckdaccccdegk";
        int code = 4;

        System.out.println(s.solution(ciper, code));
    }

    public String solution(String cipher, int code) {
        String answer = "";

        for (int i = code; i < cipher.length() + 1; i += code) {
            answer += cipher.charAt(i-1);
        }

        return answer;
    }
}
