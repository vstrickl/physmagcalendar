import React from 'react';
import ReactDOM from 'react-dom/client';
import FullCalendar from '@fullcalendar/react';
import timeGridPlugin from '@fullcalendar/timegrid'

const CalendarComponent = () => {
    const studio_id = import.meta.env.VITE_STUDIO_CALENDAR_ID;
    const von_privates_id = import.meta.env.VITE_VONS_PRIVATES_ID;

    return (
        <FullCalendar
            plugins={[timeGridPlugin]}
            initialView="timeGridWeek"
            headerToolbar={{
                left: 'prev',
                center: 'Martial Arts Studio',
                right: 'timeGridWeek,timeGridFourDay,timeGridDay,next'
            }}
            events={(info, successCallback, failureCallback) => {
                // Check if calendar IDs are defined before making requests
                if (!studio_id || !von_privates_id) {
                    console.error('Calendar IDs not found in environment variables');
                    failureCallback(new Error('Calendar IDs not configured'));
                    return;
                }

                // Fetch events for both calendars
                Promise.all([
                    fetch(`/studio/api/calendar/${encodeURIComponent(studio_id)}/`),
                    fetch(`/studio/api/calendar/${encodeURIComponent(von_privates_id)}/`)
                ])
                .then(async responses => {
                    for (const response of responses) {
                        if (!response.ok) {
                            const text = await response.text();
                            console.error('Response not OK:', {
                                status: response.status,
                                statusText: response.statusText,
                                body: text
                            });
                            throw new Error(`HTTP error! status: ${response.status}`);
                        }
                    }
                    return Promise.all(responses.map(res => res.json()));
                })
                .then(([studioEvents, privateEvents]) => {
                    console.log('Received events:', {
                        studio: studioEvents,
                        private: privateEvents
                    });

                    const formattedEvents = [...studioEvents, ...privateEvents].map(event => ({
                        title: event.summary,
                        start: event.start.dateTime || event.start.date,
                        end: event.end.dateTime || event.end.date,
                        description: event.description,
                        location: event.location,
                    }));
                    
                    console.log('Formatted events:', formattedEvents);
                    successCallback(formattedEvents);
                })
                .catch(error => {
                    console.error('Error fetching calendar events:', error);
                    failureCallback(error);
                });
            }}
        />
    );
};

const root = ReactDOM.createRoot(document.getElementById('react-calendar'));
root.render(<CalendarComponent />);
