import { Switch, Route, Redirect } from 'react-router-dom';

import Profile from './pages/Profile'


// Font Awesome Style Sheet
import '@fortawesome/fontawesome-free/css/all.min.css';

// Tailwind CSS Style Sheet
import './assets/styles/tailwind.css';

function App() {
    return (
        <Switch>

            <Route exact path="/" component={Profile} />

            <Redirect from="*" to="/" />
        </Switch>
    );
}

export default App;
