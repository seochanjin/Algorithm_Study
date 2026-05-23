import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String inputLine = br.readLine();
        String exLine = br.readLine();
        
        if (inputLine == null || exLine == null) return;

        char[] str = inputLine.toCharArray();
        char[] explosion = exLine.toCharArray();
        
        // 괄호 제거! (배열의 속성이므로)
        int expLen = explosion.length; 

        // 괄호 제거!
        char[] result = new char[str.length]; 
        int idx = 0;

        // 괄호 제거!
        for (int i = 0; i < str.length; i++) { 
            result[idx++] = str[i];

            if (idx >= expLen) {
                boolean isMatch = true;

                for (int j = 0; j < expLen; j++) {
                    if (result[idx - expLen + j] != explosion[j]) {
                        isMatch = false;
                        break;
                    }
                }
                
                if (isMatch) {
                    idx -= expLen;
                }
            }
        }

        if (idx == 0) {
            System.out.println("FRULA");
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < idx; i++) {
                sb.append(result[i]);
            }
            System.out.println(sb.toString());
        }
    }
}