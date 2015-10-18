package ninja.fridge.fridgeninja;

import java.util.Collection;
import java.util.List;

/**
 * Created by Benedikt on 17.10.2015.
 */
public interface MatchedBeaconUpdateCallback {
    public void beaconsChanged(List<BeaconBuffer.BeaconInfo> newBeacons);
}
