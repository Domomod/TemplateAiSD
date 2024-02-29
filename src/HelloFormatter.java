import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class HelloFormatter {
    public static String getFormattedHello() {
        // Format the date and time using a DateTimeFormatter
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        LocalDateTime currentDateTime = LocalDateTime.now();
        String formattedDateTime = currentDateTime.format(formatter);

        return "Hello, World! Today is " + formattedDateTime + "!";
    }
}
