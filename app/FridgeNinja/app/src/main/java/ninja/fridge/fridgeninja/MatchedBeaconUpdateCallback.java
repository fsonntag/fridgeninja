package ninja.fridge.fridgeninja;

import java.util.Collection;

/**
 * Created by Benedikt on 17.10.2015.
 */
public interface MatchedBeaconUpdateCallback {
    public void beaconsChanged(Collection<BeaconBuffer.BeaconInfo> newBeacons);
}
