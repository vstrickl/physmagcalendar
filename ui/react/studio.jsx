import React from 'react';
import ReactDOM from 'react-dom/client';
import FullCalendar from '@fullcalendar/react';
import timeGridPlugin from '@fullcalendar/timegrid'
import googleCalendarPlugin from '@fullcalendar/google-calendar';

const CalendarComponent = () => {
    const calendarApiKey = 'YOUR_GOOGLE_CALENDAR_API_KEY';
    const calendarIds = [
        'first-calendar-id@group.calendar.google.com',
        'second-calendar-id@group.calendar.google.com',
    ];

    return (
        <FullCalendar
            plugins={[
                timeGridPlugin,
                googleCalendarPlugin
            ]}
            initialView="timeGridWeek"
            googleCalendarApiKey={calendarApiKey}
            events={[
                { googleCalendarId: calendarIds[0] },
                { googleCalendarId: calendarIds[1] },
            ]}
        />
    );
};

const root = ReactDOM.createRoot(document.getElementById('react-calendar'));
root.render(<CalendarComponent />);
