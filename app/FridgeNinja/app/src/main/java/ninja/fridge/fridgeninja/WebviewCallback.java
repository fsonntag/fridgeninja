package ninja.fridge.fridgeninja;

/**
 * Created by Benedikt on 17.10.2015.
 */
public interface WebviewCallback {
    void navigateTo(String url);
    void reload();
}
