package ninja.fridge.fridgeninja;

import android.app.Activity;
import android.net.Uri;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import android.webkit.WebChromeClient;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;

import java.util.Collection;


/**
 * A simple {@link Fragment} subclass.
 * Use the {@link MountedModeFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class MountedModeFragment extends Fragment implements WebviewCallback, MatchedBeaconUpdateCallback {

    private MainActivity mainActivity;
    private WebView webview;

    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     *
     * @return A new instance of fragment MountedModeFragment.
     */
    public static MountedModeFragment newInstance() {
        MountedModeFragment fragment = new MountedModeFragment();
        Bundle args = new Bundle();
        fragment.setArguments(args);
        return fragment;
    }

    public MountedModeFragment() {
        // Required empty public constructor
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
//        if (getArguments() != null) {
//            mParam1 = getArguments().getString(ARG_PARAM1);
//            mParam2 = getArguments().getString(ARG_PARAM2);
//        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_mounted_mode, container, false);
        webview = (WebView)view.findViewById(R.id.webview);

        // Inflate the layout for this fragment
        final Activity activity = mainActivity;
        webview.setWebChromeClient(new WebChromeClient() {
            public void onProgressChanged(WebView view, int progress) {
                // Activities and WebViews measure progress with different scales.
                // The progress meter will automatically disappear when we reach 100%
                activity.setProgress(progress * 1000);
            }
        });
        webview.setWebViewClient(new WebViewClient() {
            public void onReceivedError(WebView view, int errorCode, String description, String failingUrl) {
                Toast.makeText(activity, "Oh no! " + description, Toast.LENGTH_SHORT).show();
            }
        });

        webview.getSettings().setJavaScriptEnabled(true);

        navigateTo("http://bbrandner.com");
        return view;
    }

    @Override
    public void onAttach(Activity activity) {
        super.onAttach(activity);
        try {
            mainActivity = (MainActivity) activity;
        } catch (ClassCastException e) {
            throw new ClassCastException(activity.toString()
                    + " must be MainActivity");
        }
    }

    @Override
    public void onDetach() {
        super.onDetach();
        mainActivity = null;
    }

    @Override
    public void beaconsChanged(Collection<BeaconBuffer.BeaconInfo> newBeacons) {
    }

    @Override
    public void navigateTo(String url) {
        webview.loadUrl(url);
    }
}
