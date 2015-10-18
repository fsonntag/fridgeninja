package ninja.fridge.fridgeninja;

import android.app.Activity;
import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.Collection;
import java.util.LinkedList;
import java.util.List;


/**
 * A simple {@link Fragment} subclass.
 * Use the {@link DiagnosisFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class DiagnosisFragment extends Fragment implements MatchedBeaconUpdateCallback, FragmentInteractionListener {
    public void setCallback(FridgeCallback callback) {
        this.callback = callback;
    }

    @Override
    public void beaconsChanged(final List<BeaconBuffer.BeaconInfo> newBeacons) {
        mActivity.runOnUiThread(new Runnable() {
            @Override
            public void run() {
                View view = getView();
                if(view != null) {
                    adapter.clear();
                    adapter.addAll(newBeacons);
                    adapter.notifyDataSetChanged();
                }
            }
        });

    }

    @Override
    public void setStatus(String status, String code) {
        if(mActivity == null) {
            return;
        }

        final String stateCopy = status;
        final String copy = code;
        mActivity.runOnUiThread(new Runnable() {
            @Override
            public void run() {
                if(getView() != null) {
                    TextView v = (TextView) getView().findViewById(android.R.id.text1);
                    v.setText(copy);
                    TextView vs = (TextView) getView().findViewById(R.id.openimg);
                    vs.setText(stateCopy);
                }
            }
        });
    }
//    // TODO: Rename parameter arguments, choose names that match
//    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
//    private static final String ARG_PARAM1 = "param1";
//    private static final String ARG_PARAM2 = "param2";
//
//    // TODO: Rename and change types of parameters
//    private String mParam1;
//    private String mParam2;

    public interface FridgeCallback {
        public void opened();
        public void closed();
        public void startOpening();
        public void startClosing();
    }

    private MainActivity mActivity;
    private FridgeCallback callback;


    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     *
     * @return A new instance of fragment FridgeInterfaceFragment.
     */
    // TODO: Rename and change types and number of parameters
    public static DiagnosisFragment newInstance() {
        DiagnosisFragment fragment = new DiagnosisFragment();
        Bundle args = new Bundle();
//        args.putString(ARG_PARAM1, param1);
//        args.putString(ARG_PARAM2, param2);
        fragment.setArguments(args);
        return fragment;
    }

    public DiagnosisFragment() {
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

    ArrayAdapter<BeaconBuffer.BeaconInfo> adapter;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view = inflater.inflate(R.layout.fragment_fridge_interface, container, false);
        ((TextView)view.findViewById(android.R.id.empty)).setText("No beacons");
        adapter = new ArrayAdapter<BeaconBuffer.BeaconInfo>(mActivity, android.R.layout.simple_list_item_2,
                android.R.id.text1, new ArrayList<BeaconBuffer.BeaconInfo>()) {
            @Override
            public View getView(int position, View convertView, ViewGroup parent) {
                View view = super.getView(position, convertView, parent);
                TextView text1 = (TextView) view.findViewById(android.R.id.text1);
                TextView text2 = (TextView) view.findViewById(android.R.id.text2);

                BeaconBuffer.BeaconInfo info = getItem(position);

                text1.setText(info.beacon.getBluetoothAddress());
                text2.setText("Distance " + info.minDistance + "m");
                return view;
            }
        };
        ((ListView)view.findViewById(android.R.id.list)).setAdapter(adapter);
        return view;
    }

    @Override
    public void onAttach(Activity activity) {
        super.onAttach(activity);

        try {
            mActivity = (MainActivity) activity;
        } catch (ClassCastException e) {
            throw new ClassCastException(activity.toString()
                    + " must be MainActivity");
        }

        mActivity.bindMatchedUpdateCallback(this);

    }

    @Override
    public void onDetach() {
        super.onDetach();
        mActivity.unbindBeaconsUpdateCallback(this);
        mActivity = null;
    }

}
