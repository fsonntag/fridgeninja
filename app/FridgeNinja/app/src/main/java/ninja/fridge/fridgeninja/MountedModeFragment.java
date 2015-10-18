package ninja.fridge.fridgeninja;

import android.app.Activity;
import android.graphics.Bitmap;
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

import org.altbeacon.beacon.Beacon;

import java.util.Collection;
import java.util.List;


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
        webview.clearCache(true);

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
                Toast.makeText(activity, "Oh no! " + description, Toast.LENGTH_LONG).show();
            }
            public void onPageStarted(WebView view, String url, Bitmap favicon) {
                Toast.makeText(activity, "Navigating, be patient :)", Toast.LENGTH_LONG).show();
            }
            public void onPageFinished(WebView view, String url) {
                Toast.makeText(activity, "Done", Toast.LENGTH_LONG).show();
            }
        });

        webview.getSettings().setJavaScriptEnabled(true);

        navigateTo("http://philippd.me");
        return view;
    }

    @Override
    public void onAttach(Activity activity) {
        super.onAttach(activity);
        try {
            mainActivity = (MainActivity) activity;
            ((MainActivity) activity).bindMatchedUpdateCallback(this);
        } catch (ClassCastException e) {
            throw new ClassCastException(activity.toString()
                    + " must be MainActivity");
        }
    }

    @Override
    public void onDetach() {
        super.onDetach();
        mainActivity.unbindBeaconsUpdateCallback((MatchedBeaconUpdateCallback) this);
        mainActivity = null;
    }

    @Override
    public void beaconsChanged(List<BeaconBuffer.BeaconInfo> newBeacons) {
        String user;
        if(newBeacons.isEmpty()) {
            user = "ninja";
        } else {
            Beacon beacon = newBeacons.get(0).beacon;
            if(!mainActivity.getUsersByDevice().containsKey(beacon.getBluetoothAddress())) {
                user = "anonymous";
            } else {
                user = mainActivity.getUsersByDevice().get(beacon.getBluetoothAddress());
            }
        }

        Toast.makeText(mainActivity, "Launching website!", Toast.LENGTH_LONG).show();
        webview.loadUrl("http://philippd.me/secret.html?username=" + user);
    }

    @Override
    public void navigateTo(String url) {
        webview.loadUrl(url);
    }
}
